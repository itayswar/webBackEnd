// רישום לקונסולה
var x;
x = "Itay Swartzstein";
console.log(x);

// קיצור עבור הביטוי QUERY SELECTOR
var select = function (s) {
  return document.querySelector(s);
}

// פונקציית עזר, מחזירה מספר בין מינ למקס, בתוספת 1
function randomBetween(min,max)
{
    var number = Math.floor(Math.random()*(max-min+1)+min);

    if ( number !== 0 ){
      return number;
    }else {
      return 0.5;
    }
}

//  דואג שכל אחד מהכדורים ישנה גדול באופן רנדומלי, על מנת ליצור אפקט של אנימציה
var tl = new TimelineMax();

for(var i = 0; i < 20; i++){

  var t = TweenMax.to(select('.bubble' + i), randomBetween(1, 1.5), {
    x: randomBetween(12, 15) * (randomBetween(-1, 1)),
    y: randomBetween(12, 15) * (randomBetween(-1, 1)),
    repeat:-1,
    repeatDelay:randomBetween(0.2, 0.5),
    yoyo:true,
    ease:Elastic.easeOut.config(1, 0.5)
  })

  tl.add(t, (i+1)/0.6)
}

tl.seek(50);

//  וואלידציה על המייל, על ידי FORM API
function validFunc() {
    const inpObj = document.getElementById("inputMail");
    if (!inpObj.checkValidity()) {
        document.getElementById("validationP").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("validationP").innerHTML = "Input OK";
    }
} 

