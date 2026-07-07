import { useState } from 'react';
import Card from './components/Card.tsx'
import SearchBar from './components/SearchBar.tsx'

function App() {
  const [search, setSearch] = useState("");
  return (
    <><div className="flex items-center justify-center  text-4xl">
      Find a Pokemon
    </div><div className="max-w-md mx-auto mt-10">

      <div className="mx-auto mt-8 max-w-lg">
      <SearchBar
        value={search}
        onChange={setSearch}
        placeholder="Search Pokémon..."
      />

      <p className="mt-4">Searching for: {search}</p>
    </div>
        <Card
          title="Pokemon"
          subtitle="Electric Type"
        >
          <p className="text-gray-700">
            Pikachu is an Electric-type Pokémon.
          </p>

          <button className="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
            View Details
          </button>
        </Card>
      </div></>
  )
}

export default App