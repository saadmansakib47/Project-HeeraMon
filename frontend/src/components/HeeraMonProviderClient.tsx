'use client';

import { HeeraMonProvider } from '@/context/HeeraMonContext';
import type { ReactNode } from 'react';

export default function HeeraMonProviderClient({ children }: { children: ReactNode }) {
  return <HeeraMonProvider>{children}</HeeraMonProvider>;
}
