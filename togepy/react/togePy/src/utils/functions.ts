export async  function searchPokemonByName(name: string) {
 const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${name.toLowerCase()}`
      );

      if (!response.ok) {
        throw new Error("Pokémon nicht gefunden");
      }
      return await response.json();
}