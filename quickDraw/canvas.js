window.addEventListener('load', ()=> {
    const canvas = document.querySelector('#canvas-board');
    const position = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');

    canvas.height = 300;
    canvas.width = 300;

    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.height, canvas.width);

    let painting = false;
    
    function startPosition(e) {
        painting = true;
        draw(e);
    }

    function endPosition() {
        painting = false;
        ctx.beginPath();
    }

    function draw(e) {
        if (!painting) return;
        ctx.lineWidth = 8;
        ctx.lineCap = 'round';
        ctx.lineTo(e.clientX - position.x, e.clientY - position.y);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(e.clientX - position.x, e.clientY - position.y);
    } 

    function preProcessString(s) {
        s = s.replace('_', ' ');
        s = s.replace('_', ' ');
        s = s.replace('_', ' ');
        s = s.replace('_', ' ');
        s = s.charAt(0).toUpperCase() + s.slice(1);
        return s;
    }

    function predictImage() {
        var d = canvas.toDataURL();
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/predict',
            data: {
                imgBase64: d
            },
            success: function(result) {
                Result = "I think it is "
                var sortable = [];
                for (const [key, value] of Object.entries(result)) {
                    sortable.push([key, value]);
                }
                sortable.sort(function(a, b) {
                    return b[1] - a[1];
                });
                sortable.forEach(element => Result += preProcessString(element[0]) + ", ");
                Result = Result.substring(0, Result.length - 2);
                document.querySelector('#result').innerHTML = Result;
            }
        });
    }

    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', () => {
        endPosition();
        predictImage();
    });

});
