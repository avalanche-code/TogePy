import { fireEvent, render, screen } from "@testing-library/react";
import { test, expect, vi } from 'vitest';
import Card from "../src/components/Card.tsx";

test("renders card title", () => {
  render(
    <Card title="Pikachu">
      Content
    </Card>
  );

  expect(
    screen.getByText("Pikachu")
  ).toBeInTheDocument();
});

test("calls onRemove when the saved-list remove button is clicked", () => {
  const handleRemove = vi.fn();

  render(
    <Card title="Pikachu" savedList onRemove={handleRemove}>
      Content
    </Card>
  );

  fireEvent.click(screen.getByRole("button", { name: /remove pokémon/i }));

  expect(handleRemove).toHaveBeenCalledTimes(1);
});