import { render, screen, fireEvent } from "@testing-library/react";
import { vi, test, expect } from 'vitest';
import SearchBar from "../src/components/SearchBar.tsx";


test("calls onChange when typing", () => {
  const handleChange = vi.fn();

  render(
    <SearchBar
      value=""
      onChange={handleChange}
      onSearch={vi.fn()}
    />
  );

  const input = screen.getByPlaceholderText(
    "Search..."
  );

  fireEvent.change(input, {
    target: {
      value: "pikachu"
    }
  });

  expect(handleChange)
    .toHaveBeenCalledWith("pikachu");
});

test("calls onSearch when pressing Enter", () => {
  const handleSearch = vi.fn();

  render(
    <SearchBar
      value="pikachu"
      onChange={vi.fn()}
      onSearch={handleSearch}
    />
  );

  const input = screen.getByPlaceholderText("Search...");
  fireEvent.keyDown(input, { key: "Enter" });

  expect(handleSearch).toHaveBeenCalledTimes(1);
});