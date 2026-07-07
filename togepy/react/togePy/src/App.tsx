import { useState } from 'react';
import Card from './components/Card.tsx'
import SearchBar from './components/SearchBar.tsx'

type Pokemon = {
  name: string;
  gender: string;
  type: string;
  attacks: string[];
  image: string;
};
function App() {
  const [search, setSearch] = useState("");
  const [savedPokemon, setSavedPokemon] = useState<Pokemon[]>([]);
  const [pokemon, setPokemon] = useState<Pokemon>({
    name: "Pikachu",
    gender: "male",
    type: "Electric",
    attacks: ["Quick Attack", "Thunderbolt"],
    image: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const[isFound, setIsFound] = useState(true);

  function capitalize(s: string) {
    return s ? s.charAt(0).toUpperCase() + s.slice(1) : s;
  }

  async function searchPokemon() {
    if (!search.trim()) return;

    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${search.toLowerCase()}`
      );

      if (!response.ok) {
        throw new Error("Pokemon not found");
      }

      const data = await response.json();

      const mapped = {
        name: capitalize(data.name || ""),
        gender: "male/female", // The API does not provide gender information
        type:
          data.types && data.types[0]
            ? capitalize(data.types[0].type.name)
            : "Unknown",
        attacks: Array.isArray(data.moves)
          ? data.moves.slice(0, 4).map((m: { move: { name: string } }) => capitalize(String(m.move.name).replace(/-/g, ' ')))
          : [],
        image:
          data.sprites?.other?.['official-artwork']?.front_default ||
          data.sprites?.front_default ||
          "",
      };

      setPokemon(mapped);
      setIsFound(true);
    } catch (err: unknown) {
      console.error(err);
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError(String(err));
      }
      setIsFound(false);
    } finally {
      setLoading(false);
    }
  }

  async function savePokemon(pokemon: Pokemon) {
    setSavedPokemon((prev) => [...prev, pokemon]);
  }

  return (
    <><div className="flex items-center justify-center  text-4xl">
      Find a Pokemon
    </div><div className="max-w-md mx-auto mt-10">

      <div className="mx-auto mt-8 max-w-lg">
      <SearchBar
        value={search}
        onChange={setSearch}
        onSearch={searchPokemon}
        placeholder="Search Pokémon..."
      />

      <p className="mt-4">Searching for: {search}</p>
    </div>
        {loading ? (
          <p className="mt-4">Loading...</p>
        ) : isFound ? (
          <Card
            title={pokemon.name}
            subtitle={`${pokemon.gender} • ${pokemon.type}`}
          >
            <div className="md:flex md:items-center md:justify-between">
              <div className="md:w-2/3">
                <p className="text-gray-700">
                  {pokemon.name} is a {pokemon.type.toLowerCase()}-type Pokémon.
                </p>

                <ul className="mt-3 list-disc pl-5 text-sm text-gray-700">
                  {pokemon.attacks.map((attack) => (
                    <li key={attack}>{attack}</li>
                  ))}
                </ul>

                <button className="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                onClick={() => savePokemon(pokemon)}>
                  Save
                </button>
              </div>

              {pokemon.image ? (
                <div className="mt-6 md:mt-0 md:ml-6 md:w-1/3 flex justify-center">
                  <img
                    src={pokemon.image}
                    alt={`${pokemon.name} sprite`}
                    className="h-32 w-32 object-contain"
                  />
                </div>
              ) : null}
            </div>
          </Card>
        ) : (
          <p className="mt-4 text-red-600">{error || 'Pokémon nicht gefunden'}</p>
        )}

        <div className="flex items-center justify-center  text-4xl mt-10" >
      Your saved Pokémon
    </div>
        {savedPokemon.length > 0 ? (
          <div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
            {savedPokemon.map((p, index) => (
              <Card
                key={index}
                title={p.name}
                subtitle={`${p.gender} • ${p.type}`}      
          >
                <div className="md:flex md:items-center md:justify-between">
                  <div className="md:w-2/3">
                    <p className="text-gray-700">
                      {p.name} is a {p.type.toLowerCase()}-type Pokémon.
                    </p>

                    <ul className="mt-3 list-disc pl-5 text-sm text-gray-700">
                      {p.attacks.map((attack: string) => (
                        <li key={attack}>{attack}</li>
                      ))}
                    </ul>
                  </div>

                  {p.image ? (
                    <div className="mt-6 md:mt-0 md:ml-6 md:w-1/3 flex justify-center">
                      <img
                        src={p.image}
                        alt={`${p.name} sprite`}
                        className="h-32 w-32 object-contain"
                      />
                    </div>
                  ) : null}
                </div>
              </Card>
            ))}
          </div>
        ) : (
          <p className="mt-4">No Pokémon saved yet.</p>
        )}
      </div></>
  )
}

export default App