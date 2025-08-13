<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Beyblade Interactif</title>
<style>
  body { font-family: Arial, sans-serif; text-align: center; padding: 20px; background: #f0f0f0; }
  button { padding: 10px 20px; font-size: 16px; margin: 10px; cursor: pointer; }
  select { font-size: 16px; padding: 5px; }
  .combat { margin-top: 20px; font-size: 18px; }
</style>
</head>
<body>

<h1>Beyblade Interactif</h1>

<label>Choisis ta toupie :</label>
<select id="maToupie">
</select>
<br>
<button onclick="lancerCombat()">Combattre !</button>

<div id="resultats" class="combat"></div>

<script>
const toupies = [
  { nom: "Flamme", puissance: 80 },
  { nom: "Glace", puissance: 75 },
  { nom: "Éclair", puissance: 85 },
  { nom: "Terre", puissance: 70 },
  { nom: "Aqua", puissance: 78 },
  { nom: "Vent", puissance: 76 },
  { nom: "Tonnerre", puissance: 82 },
  { nom: "Roc", puissance: 74 }
];

// Remplir le menu déroulant
const select = document.getElementById("maToupie");
toupies.forEach((t, i) => {
  const option = document.createElement("option");
  option.value = i;
  option.text = t.nom;
  select.add(option);
});

function duel(t1, t2) {
  const total1 = t1.puissance + Math.floor(Math.random()*20);
  const total2 = t2.puissance + Math.floor(Math.random()*20);
  return total1 >= total2 ? t1 : t2;
}

function lancerCombat() {
  const indexJoueur = parseInt(select.value);
  const toupieJoueur = toupies[indexJoueur];

  // Choisir une toupie aléatoire pour l'ordi (différente de celle du joueur)
  let indexOrdi;
  do { indexOrdi = Math.floor(Math.random() * toupies.length); } while(indexOrdi === indexJoueur);
  const toupieOrdi = toupies[indexOrdi];

  const gagnant = duel(toupieJoueur, toupieOrdi);

  const totalJ = toupieJoueur.puissance + Math.floor(Math.random()*20);
  const totalO = toupieOrdi.puissance + Math.floor(Math.random()*20);

  document.getElementById("resultats").innerHTML =
    `Ton combat : <b>${toupieJoueur.nom}</b> (${totalJ} pts) vs <b>${toupieOrdi.nom}</b> (${totalO} pts)<br>` +
    `<h2>Gagnant : ${gagnant.nom} 🏆</h2>`;
}
</script>

</body>
</html>
