'use client';

import React from 'react';
import Image from 'next/image';
import { Feather, Compass } from 'lucide-react';

interface BirdCompanionProps {
  statusText?: string;
  isThinking?: boolean;
}

export const BirdCompanion: React.FC<BirdCompanionProps> = ({
  statusText = 'Watching for opportunities that fit your life',
  isThinking = false,
}) => {
  return (
    <div className="bg-gradient-to-r from-amber-50/80 via-white to-emerald-50/60 border border-amber-200/70 rounded-2xl p-4 shadow-sm flex items-center justify-between gap-4">
      <div className="flex items-center gap-3.5">
        <div className="relative w-14 h-14 rounded-full bg-white border-2 border-amber-300 shadow-md p-1 flex-shrink-0 flex items-center justify-center overflow-hidden">
          <Image
            src="/images/HeeraMon-Transparent.png"
            alt="HeeraMon Wisdom Companion"
            width={52}
            height={52}
            className={`object-contain transition-transform duration-500 ${
              isThinking ? 'scale-105 animate-pulse' : 'hover:scale-110'
            }`}
          />
          {isThinking && (
            <span className="absolute bottom-0 right-0 w-3.5 h-3.5 bg-amber-500 rounded-full border-2 border-white animate-ping" />
          )}
        </div>

        <div>
          <div className="flex items-center gap-2">
            <h3 className="font-semibold text-sm text-foreground flex items-center gap-1.5">
              <span>HeeraMon</span>
              <Feather className="w-3.5 h-3.5 text-amber-600" />
            </h3>
            <span className="text-[11px] font-medium px-2 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-200 flex items-center gap-1">
              <span className={`w-1.5 h-1.5 rounded-full ${isThinking ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500'}`} />
              {isThinking ? 'Contemplating...' : 'Vigilant'}
            </span>
          </div>
          <p className="text-xs text-muted mt-0.5 line-clamp-1">{statusText}</p>
        </div>
      </div>

      <div className="hidden sm:flex items-center gap-1.5 text-xs text-neutral-500 bg-white/80 border border-neutral-200/80 px-2.5 py-1 rounded-lg">
        <Compass className="w-3.5 h-3.5 text-emerald-600" />
        <span>Fit over Volume</span>
      </div>
    </div>
  );
};
