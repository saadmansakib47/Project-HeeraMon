import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        nunito: ['Nunito', 'sans-serif'],
      },
    },
    // existing extend block will be merged

    extend: {
      colors: {
        background: "#fafafa",
        surface: "#ffffff",
        foreground: "#111827",
        muted: "#6b7280",
        border: "#e5e7eb",
        bird: {
          emerald: "#059669",
          amber: "#d97706",
          gold: "#f59e0b",
          coral: "#f43f5e"
        }
      },
      borderRadius: {
        'card': '12px',
      }
    },
  },
  plugins: [],
};
export default config;
