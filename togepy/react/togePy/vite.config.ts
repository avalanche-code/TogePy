/// <reference types="vitest/config" />

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],

  base: "/TogePy/",

  test: {
    globals: true,
    environment: "jsdom",
    exclude: [
      "tests/**",              // Playwright Tests ignorieren
      "**/node_modules/**",
    ],
    coverage: {
      provider: "v8",
      reporter: [
        ["text", { skipFull: true }],
        "html",
        "lcov",
      ],
    },
  },
});