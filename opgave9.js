let leeftijd = parseInt(prompt("Hoe oud ben je?"));
let rijbewijs = prompt("Heb je een rijbewijs? (ja/nee)").toLowerCase();

if (leeftijd >= 18 & rijbewijs == "ja")
    console.log("jij mag auto rijden")
else
    console.log("jij mag geen auto rijden");
    