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
  const [isFound, setIsFound] = useState(true);
  const [saveEnabled, setSaveEnabled] = useState(false);

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
        throw new Error("Pokémon nicht gefunden");
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
      setSaveEnabled(true);
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
    setSaveEnabled(false);
    setSavedPokemon((prev) => [...prev, pokemon]);
  }

  return (
    <><h1 className="flex items-center justify-center  text-4xl" test-id="title">
      Find a Pokémon
    </h1><div className="mx-auto mt-10 max-w-5xl px-4">

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
          test-id="pokemon-card">
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

                <div>
                  
                  <button
                    className={`mt-4 rounded-lg bg-blue-600 px-4 py-2 text-white  }`}
                    disabled={!saveEnabled}
                    onClick={() => savePokemon(pokemon)}
                   // hand cursor only when saveEnabled is true
                    style={{ cursor: saveEnabled ? 'pointer' : 'not-allowed' }}
                 id="save-button" >
                    Save
                  </button>
                  {!saveEnabled ? (<p className="text-red-600 text-sm" >Save disabled make a search first</p>) : null}
                </div>
              </div>

              {pokemon.image ? (
                <div className="mt-6 flex justify-center md:mt-0 md:ml-6 md:w-1/3">
                  <img
                    src={pokemon.image}
                    alt={`${pokemon.name} sprite`}
                    className="h-36 w-36 object-contain md:h-44 md:w-44"
                  />
                </div>
              ) : null}
            </div>
          </Card>
        ) : (
          <p className="mt-4 text-red-600">{error || 'Pokémon nicht gefunden'}</p>
        )}

        <h2 className="flex items-center justify-center  text-4xl mt-10" data-testid="title">
          Your saved Pokémon
        </h2>
        {savedPokemon.length > 0 ? (
          <div className="mt-4 grid grid-cols-1 gap-6 sm:grid-cols-2 xl:grid-cols-3" data-testid="saved-pokemon-list">
            {savedPokemon.map((p, index) => (
              <Card
                key={index}
                title={p.name}
                subtitle={`${p.gender} • ${p.type}`}
                className="h-full min-h-[280px]"
              >
                <div className="flex flex-col items-center gap-4 md:flex-row md:items-start md:justify-between">
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
                    <div className="flex justify-center md:ml-6 md:w-1/3">
                      <img
                        src={p.image}
                        alt={`${p.name} sprite`}
                        className="h-36 w-36 object-contain md:h-44 md:w-44"
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