
'use client';

import React from 'react';
import Image from 'next/image';
import { Bell, Sparkles, SlidersHorizontal, Briefcase, MessageSquare } from 'lucide-react';

interface NavbarProps {
  activeTab: 'chat' | 'opportunities' | 'preferences';
  setActiveTab: (tab: 'chat' | 'opportunities' | 'preferences') => void;
  matchesCount: number;
  preferencesCount: number;
  unreadNotificationsCount: number;
  onOpenNotifications: () => void;
  onTriggerSearch: () => void;
  isSearching: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  matchesCount,
  preferencesCount,
  unreadNotificationsCount,
  onOpenNotifications,
  onTriggerSearch,
  isSearching,
}) => {
  return (
    <header className="sticky top-0 z-30 bg-surface/90 backdrop-blur-md border-b border-border/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand identity */}
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => setActiveTab('chat')}>
          <div className="relative w-10 h-10 rounded-full overflow-hidden border border-amber-300 shadow-sm bg-gradient-to-tr from-amber-50 to-emerald-50 flex items-center justify-center">
            <Image
              src="/images/HeeraMon-Transparent.png"
              alt="HeeraMon Wisdom Bird"
              width={38}
              height={38}
              className="object-contain"
              priority
            />
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-bold text-lg text-foreground tracking-tight">HeeraMon</span>
              <span className="text-[10px] font-semibold tracking-wider uppercase px-1.5 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-200">
                Wisdom Bird
              </span>
            </div>
            <p className="text-xs text-muted -mt-0.5">Continuous job-seeking intelligence</p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="hidden md:flex items-center gap-1 bg-neutral-100 p-1 rounded-xl border border-neutral-200">
          <button
            onClick={() => setActiveTab('chat')}
            className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'chat'
                ? 'bg-white text-foreground shadow-sm'
                : 'text-neutral-600 hover:text-foreground'
            }`}
          >
            <MessageSquare className="w-4 h-4 text-emerald-600" />
            <span>Dialogue</span>
          </button>

          <button
            onClick={() => setActiveTab('opportunities')}
            className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'opportunities'
                ? 'bg-white text-foreground shadow-sm'
                : 'text-neutral-600 hover:text-foreground'
            }`}
          >
            <Briefcase className="w-4 h-4 text-amber-600" />
            <span>Opportunities</span>
            {matchesCount > 0 && (
              <span className="text-xs bg-amber-100 text-amber-800 px-1.5 py-0.2 rounded-full font-semibold">
                {matchesCount}
              </span>
            )}
          </button>

          <button
            onClick={() => setActiveTab('preferences')}
            className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeTab === 'preferences'
                ? 'bg-white text-foreground shadow-sm'
                : 'text-neutral-600 hover:text-foreground'
            }`}
          >
            <SlidersHorizontal className="w-4 h-4 text-neutral-600" />
            <span>Preferences</span>
            {preferencesCount > 0 && (
              <span className="text-xs bg-neutral-200 text-neutral-700 px-1.5 py-0.2 rounded-full font-semibold">
                {preferencesCount}
              </span>
            )}
          </button>
        </nav>

        {/* Action Controls */}
        <div className="flex items-center gap-2.5">
          {/* Continuous Search Button */}
          <button
            onClick={onTriggerSearch}
            disabled={isSearching}
            className="flex items-center gap-2 px-3 py-1.5 text-xs font-semibold text-neutral-800 bg-neutral-50 hover:bg-neutral-100 border border-neutral-300 rounded-lg shadow-sm transition-all disabled:opacity-50"
            title="Trigger background search cycle across job sources"
          >
            <Sparkles className={`w-3.5 h-3.5 text-amber-500 ${isSearching ? 'animate-spin' : ''}`} />
            <span className="hidden sm:inline">{isSearching ? 'Scouting...' : 'Scout Horizon'}</span>
          </button>

          {/* Notification Bell */}
          <button
            onClick={onOpenNotifications}
            className="relative p-2 rounded-lg text-neutral-600 hover:text-neutral-900 hover:bg-neutral-100 transition-colors border border-transparent hover:border-neutral-200"
            aria-label="View notifications"
          >
            <Bell className="w-4 h-4" />
            {unreadNotificationsCount > 0 && (
              <span className="absolute top-1 right-1 w-2.5 h-2.5 bg-rose-500 rounded-full ring-2 ring-white animate-pulse" />
            )}
          </button>
        </div>

      </div>
    </header>
  );
};

export default Navbar;
