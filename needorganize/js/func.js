/*********
 * this, call(), apply(), bind()
 *********/
var pokemon = {
  firstname: "Pika",
  lastname: "Chu ",
  getPokeName: function () {
    var fullname = this.firstname + " " + this.lastname;
    return fullname;
  },
};
const pokemonName = function (snack, hobby) {
  console.log(this.getPokeName() + "I choose you!");
  console.log(this.getPokeName() + " loves " + snack + " and " + hobby);
};
//call()
// pokemonName.call(pokemon, "uu", "smith");
//apply() same result as call()
// pokemonName.apply(pokemon, ["uu", "smith"]);
//bind() same result as above
// const logPokemon = pokemonName.bind(pokemon);
// logPokemon("uu", "smith");
