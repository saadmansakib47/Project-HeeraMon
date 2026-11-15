
import './globals.css';
import type { ReactNode } from 'react';
import HeeraMonProviderClient from '@/components/HeeraMonProviderClient';

export const metadata = {
  title: 'HeeraMon',
  description: 'AI‑powered personal job‑seeking assistant',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-gray-800 antialiased">
        <HeeraMonProviderClient>{children}</HeeraMonProviderClient>
      </body>
    </html>
  );
}

