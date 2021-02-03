<?php
try
{
    $bdd = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles;charset=utf8', 'root', '');
    $bdd->query("SET lc_time_names = 'fr_FR'");
    $ville=htmlspecialchars($_GET['ville']);
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}
 
$reponse = $bdd->prepare("SELECT temperature, DATE_FORMAT(last_update,'Le %d %M %Y à %H h %i') as last_update, ville FROM temperaturevilles WHERE ville = ? ");
$reponse->execute(array($_GET['ville']));
 
while ($donnees = $reponse->fetch())
{
   /* echo  'A ',$donnees['ville'], ' il fait actuellement ',$donnees['temperature'] . '<br />';*/
    echo  $donnees['last_update'], ' il faisait ',$donnees['temperature'], '°c à ', ucfirst($donnees['ville']),'<br />';
}
 
$reponse->closeCursor();
 
?>
