import './globals.css';
import type { ReactNode } from 'react';
import { HeeraMonProvider } from '@/context/HeeraMonContext';

export const metadata = {
  title: 'HeeraMon',
  description: 'AI‑powered personal job‑seeking assistant',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-800 antialiased">
        <HeeraMonProvider>{children}</HeeraMonProvider>
      </body>
    </html>
  );
}
