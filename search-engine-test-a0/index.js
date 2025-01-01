
// 최초 크롤링 작업
// 각 사이트를 방문해 모든 <a> 다른 사이트로 이동하는 태그
// 해당 사이트로 접근
// 해당 사이트의 정보들을 인덱싱
// 해당 사이트에 있는 정보를 DB에 저장
// 다시 해당 사이트의 <a> 태그를 찾아서 다른 사이트를 이동
// 반복

const cheerio = require("cheerio");
const axios = require("axios");
const fs = require("fs");
const initUrl = 'https://en.wikipedia.org';

// 무한루프 함수
// 1. 특정 사이트 방문
// 2. 그 사이트에서 HTML 문서를 파싱
// 3. 우리가 원하는 데이터만 추출 -> DB 저장(fs로 저장, db.json)
// 4. 다음 방문할 사이트 목록을 획득 -> 참조된 사이트들은 랭크 점수를 획득
// 5. 1번으로 돌아가 반복

let dbList = {
    "https://en.wikipedia.org/wiki/Computer" : {
    title: "Computer",
    // keywords: ["computer", "hardware", "software"],
    score: 1,
    },
}; // 기존 배열 형태면 무한 반복, 객체로 변경 필요
// 예외 처리 필요 추가 (queryString)

let queue = [];
let progressIndex = 0;

const crawl = async (url) => {
    console.log("방문한 URL: ", url);

    try {
        var htmlDoc = await axios.get(url); 
    } catch (error) {    // 2번째 에러 : HTML 문서를 가져오는 과정에서 에러가 발생한 경우
        await startNextQueue();
        return;
    } 

    if (!htmlDoc.data) {    // 1. 최초 에러 : HTML 문서가 없는 경우
        await startNextQueue();
        return;
    }

    const $ = cheerio.load(htmlDoc.data); // 일종의 컨벤션
    const links = $('a');
    const title = $("h1").text();

    if (dbList[url]) {
        dbList[url].score += 1;
    } else {
        dbList[url] = {
            title,
            score: 1,
        };
    }

    links.each((index, element) => {
        const href = $(element).attr("href");

        // 만약에 href가 http:// 또는 https:// 로 시작한다면 바로 새로운 URL로 인식
        // 설정해서 crawl 함수를 호출

        // 그러나 그렇지 않은 경우라면 현재 URL 기준으로 새로운 URL을 만들어줘야 함
        // 예를 들어 현재 URL이 https://ko.wikipedia.org/wiki/Computer 라면
        // href가 /wiki/Software 라면 https://ko.wikipedia.org/wiki/Software 로 만들어줘야 함

        if (!href) return;

        if (href.startsWith("http://") || href.startsWith("https://")) {
            checkAlreadyVisited(href);
            return;
        }

        const originUrl = new URL(url).origin;
        const newUrl = originUrl + href;
        queue.push(newUrl);
    });

    if (queue[progressIndex]) {
        await startNextQueue();
    } else {
        console.log("크롤링 종료");
        console.log(dbList);
    }
};

// 이미 방문한 사이트라면 큐에 추가하지 않음
const checkAlreadyVisited = (href) => {
    if (!dbList[href]) {
        queue.push(href);
    }
};

// 큐에 있는 다음 사이트를 방문한다
const startNextQueue = async () => {    // 에러가 생겼을 때 크롤링이 멈추는 것을 방지하기 위해 async 사용
    await timeout();
    crawl(queue[progressIndex]);
    progressIndex += 1;
    if (progressIndex % 10 === 0) {
        storeDb();
    } 
};

// 딜레이를 주는 함수
const timeout = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve();
        }, 500);
    });
}

// 크롤링한 데이터를 파일로 저장하는 함수
const storeDb = () => {
    const json = JSON.stringify(dbList);
    fs.writeFileSync("./db.json", json);
};

crawl(initUrl);

// 연산 횟수가 처음엔 1개, 지수적으로 폭등
// 하위 링크가 10개

// 페이지 랭크

// a,b,c 라는 사이트에서 모두 d 사이트 링크가 있다면
// d 사이트는 인기가 있다고 볼 수 있음