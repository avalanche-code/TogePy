import { useState } from 'react';
import Card from './components/Card.tsx'
import SearchBar from './components/SearchBar.tsx'

function App() {
  const [search, setSearch] = useState("");
  const [savedPokemon, setSavedPokemon] = useState([]);
  const [pokemon, setPokemon] = useState({
    name: "Pikachu",
    gender: "male",
    type: "Electric",
    attacks: ["Quick Attack", "Thunderbolt"],
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
        gender: "unknown",
        type:
          data.types && data.types[0]
            ? capitalize(data.types[0].type.name)
            : "Unknown",
        attacks: Array.isArray(data.moves)
          ? data.moves.slice(0, 4).map((m: any) => capitalize(String(m.move.name).replace(/-/g, ' ')))
          : [],
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
            <p className="text-gray-700">
              {pokemon.name} is a {pokemon.type.toLowerCase()}-type Pokémon.
            </p>

            <ul className="mt-3 list-disc pl-5 text-sm text-gray-700">
              {pokemon.attacks.map((attack) => (
                <li key={attack}>{attack}</li>
              ))}
            </ul>

            <button className="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
              Save
            </button>
          </Card>
        ) : (
          <p className="mt-4 text-red-600">{error || 'Pokémon nicht gefunden'}</p>
        )}

        <div className="flex items-center justify-center  text-4xl mt-10" >
      Your saved Pokémon
    </div>
      </div></>
  )
}

export default App