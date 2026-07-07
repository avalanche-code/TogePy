import { Search } from "lucide-react";

type SearchBarProps = {
  value: string;
  onChange: (value: string) => void;
  onSearch: () => void;
  placeholder?: string;
};

export default function SearchBar({
  value,
  onChange,
  onSearch,
  placeholder = "Search...",
}: SearchBarProps) {
  return (
    <div className="relative w-full">
      <Search
        size={18}
        className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
      />

      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            onSearch();
          }
        }}
        placeholder={placeholder}
        className="
          w-full
          rounded-xl
          border
          border-gray-300
          bg-white
          py-2.5
          pl-10
          pr-4
          text-gray-900
          placeholder:text-gray-400
          shadow-sm
          outline-none
          transition
          focus:border-red-500
          focus:ring-2
          focus:ring-red-200
        "
      />
    </div>
  );
}