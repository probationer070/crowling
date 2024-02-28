var pretag = document.getElementById('d');     // HTML에서 pre 태그에 해당하는 요소를 가져옵니다.
    var tmr1 = undefined;                       // 애니메이션을 제어할 타이머 변수입니다.
    var A = 1, B = 1;

    var asciiframe = function () {
        var b = []; // 문자열 배열을 초기화합니다.
        var z = []; // Z-버퍼를 초기화합니다.
        A += 0.07;
        B += 0.03;
        
        var cA = Math.cos(A), sA = Math.sin(A),    // A, B 값에 변화를 주어 애니메이션을 만듭니다.
            cB = Math.cos(B), sB = Math.sin(B);

         // 도넛 차트의 각 문자 위치에 대한 계산을 수행합니다.
        for (var k = 0; k < 1760; k++) {         
            b[k] = k % 80 == 79 ? "\n" : " ";         // k가 79의 배수이면 줄 바꿈 문자를 추가하고, 아니면 공백을 추가합니다.
            z[k] = 0;                                 // Z-버퍼를 초기화합니다.
        }

        for (var j = 0; j < 6.28; j += 0.07) {        // 도넛 차트를 그리기 위한 이중 루프입니다.
            var ct = Math.cos(j), st = Math.sin(j);

            for (var i = 0; i < 6.28; i += 0.02) {
                var sp = Math.sin(i), cp = Math.cos(i),
                    h = ct + 2,
                    D = 1 / (sp * h * sA + st * cA + 5),  // D는 1/z 값입니다.
                    t = sp * h * cA - st * sA;

                // 도넛 차트의 각 문자의 화면상 위치를 계산합니다.
                var x = 0 | (40 + 30 * D * (cp * h * cB - t * sB)),
                    y = 0 | (11 + 15 * D * (cp * h * sB + t * cB)), // 조정된 y 값
                    o = x + 80 * y,
                    // 문자의 인덱스를 계산합니다.
                    N = 0 | (8 * ((st * sA - sp * ct * cA) * cB - sp * ct * sA - st * cA - cp * ct * sB));

                
                // 화면 상의 유효한 위치인 경우에만 Z-버퍼를 업데이트하고 문자를 추가합니다.
                if (y < 22 && y >= 0 && x >= 0 && x < 79 && D > z[o]) {
                    z[o] = D;
                    b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];                    // 특정 문자로 대체합니다.
                }
            }
        }
        // HTML의 pre 태그에 도넛 차트를 추가합니다.
        pretag.innerHTML = b.join("");
    };

    window.toggleAnimation = function () {
        if (tmr1 === undefined) {
            tmr1 = setInterval(asciiframe, 50);
        } else {
            clearInterval(tmr1);
            tmr1 = undefined;
        }
    };

    asciiframe();