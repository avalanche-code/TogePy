import { test, expect } from '@playwright/test';

test.describe('Pokemon app', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('shows the initial page content', async ({ page }) => {
    await expect(page).toHaveTitle('togepy');
    await expect(page.getByRole('heading', { name: /Find a Pokémon/i })).toBeVisible();
    await expect(page.getByRole('heading', { name: /Your saved Pokémon/i })).toBeVisible();
  });

  test('searches an existing Pokémon and shows its image', async ({ page }) => {
    const pokemonName = 'pikachu';

    await page.getByPlaceholder('Search Pokémon...').fill(pokemonName);
    await page.getByPlaceholder('Search Pokémon...').press('Enter');

    await expect(page.getByText(new RegExp(`Searching for: ${pokemonName}`, 'i'))).toBeVisible();
    await expect(page.getByText(/Loading/i)).toBeVisible({ timeout: 1000 });
    await expect(page.getByRole('heading', { name: /Pikachu/i })).toBeVisible();
    await expect(page.getByRole('img', { name: /pikachu sprite/i })).toBeVisible();
  });

  test('shows an error for a non-existing Pokémon', async ({ page }) => {
    await page.getByPlaceholder('Search Pokémon...').fill('notapokemon');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');

    await expect(page.getByText(/Pokémon nicht gefunden/i)).toBeVisible();
  });

  test('saves a found Pokémon', async ({ page }) => {
    await page.getByPlaceholder('Search Pokémon...').fill('pikachu');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');

    await expect(page.getByRole('button', { name: 'Save' })).toBeEnabled();
    await page.getByRole('button', { name: 'Save' }).click();
    await expect(page.getByText("No Pokémon saved yet.")).not.toBeVisible();
    await expect(page.getByTestId('saved-pokemon-list')).toContainText('Pikachu');
  });

  test('deletes a saved Pokémon', async ({ page }) => {
    await page.getByPlaceholder('Search Pokémon...').fill('pikachu');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');

    await page.getByRole('button', { name: 'Save' }).click();
    await page.getByRole('button', { name: 'Remove Pokémon' }).click();

    await expect(page.getByTestId('saved-pokemon-list')).not.toContainText('Pikachu');
  });
  test('removes all saved Pokémon', async ({ page }) => {
    const savedPokemonListLocator = page.getByTestId('saved-pokemon-list');
    await page.getByPlaceholder('Search Pokémon...').fill('pikachu');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');
    await page.getByRole('button', { name: 'Save' }).click();
    await page.getByPlaceholder('Search Pokémon...').fill('raichu');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');
    await page.getByRole('button', { name: 'Save' }).click();
    await expect(page.getByTestId("saved-pokemon-pikachu")).toBeVisible();
    await page
      .getByTestId("saved-pokemon-pikachu")
      .getByRole("button", { name: "Remove Pokémon" })
      .click();
    await page
      .getByTestId("saved-pokemon-raichu")
      .getByRole("button", { name: "Remove Pokémon" })
      .click();


    await expect(savedPokemonListLocator).not.toContainText('Pikachu');
    await expect(savedPokemonListLocator).not.toContainText('Raichu');
    await expect(savedPokemonListLocator).toContainText('No Pokémon saved yet.');
  });
  test('shows an alert when saving an already saved Pokémon', async ({ page }) => {
    await page.getByPlaceholder('Search Pokémon...').fill('pikachu');
    await page.getByPlaceholder('Search Pokémon...').press('Enter');

    await page.getByRole('button', { name: 'Save' }).click();

    page.once('dialog', async (dialog) => {
      expect(dialog.message()).toContain('already saved');
      await dialog.accept();
    });
    await page.getByPlaceholder('Search Pokémon...').press('Enter');// Search again for the same Pokémon cause field is not cleared after search
    await page.getByRole('button', { name: 'Save' }).click();
  });
});

