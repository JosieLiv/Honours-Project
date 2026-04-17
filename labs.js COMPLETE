/* JavaScript file for lab tasks */


/* REVEAL HINTS FUNCTION */
hintCount = 0
function revealHint() {
    const hints = document.querySelectorAll('.hint');
    if (hintCount < hints.length) {
        hints[hintCount].style.display = 'block';
        hintCount++;
    }
    if (hintCount === hints.length) {
        /* Change the button text if there are no more hints */
        document.querySelector('button[onclick="revealHint()"]').innerText = 'That was your last hint.';
        document.querySelector('button[onclick="revealHint()"]').disabled = true;
    }
}


/* REVEAL SOLUTION FUNCTION */
 function revealSolution() {
    const solution = document.getElementById('solution');
    const button = document.querySelector('button[onclick="revealSolution"]');
    solution.style.display = 'block';
 }
