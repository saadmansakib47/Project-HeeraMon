'use client';

import React, { useState } from 'react';
import { UserPreference, PreferenceType } from '../types';
import { ShieldCheck, Sparkles, Brain, Trash2, Plus, SlidersHorizontal, ArrowLeft } from 'lucide-react';

interface PreferencesPanelProps {
  preferences: UserPreference[];
  onUpdatePreference: (id: string, updates: Partial<UserPreference>) => Promise<void>;
  onDeletePreference: (id: string) => Promise<void>;
  onCreatePreference: (pref: Partial<UserPreference>) => Promise<void>;
  onBackToChat: () => void;
}

export const PreferencesPanel: React.FC<PreferencesPanelProps> = ({
  preferences,
  onUpdatePreference,
  onDeletePreference,
  onCreatePreference,
  onBackToChat,
}) => {
  const [showAddForm, setShowAddForm] = useState(false);
  const [newCategory, setNewCategory] = useState('salary');
  const [newValue, setNewValue] = useState('');
  const [newType, setNewType] = useState<PreferenceType>('soft');

  const hardPrefs = preferences.filter((p) => p.preference_type === 'hard');
  const softPrefs = preferences.filter((p) => p.preference_type === 'soft');
  const learnedPrefs = preferences.filter((p) => p.preference_type === 'learned');

  const handleAddSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newValue.trim()) return;
    await onCreatePreference({
      category: newCategory,
      value: newValue.trim(),
      preference_type: newType,
      source: 'explicit',
      confidence: 1.0,
      status: 'active',
    });
    setNewValue('');
    setShowAddForm(false);
  };

  const renderPreferenceCard = (pref: UserPreference) => {
    return (
      <div
        key={pref.id}
        className="bg-white border border-neutral-200/90 rounded-xl p-3.5 shadow-2xs hover:border-neutral-300 transition-all flex items-center justify-between gap-3"
      >
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider text-neutral-500">
              {pref.category.replace('_', ' ')}
            </span>
            <span
              className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${
                pref.preference_type === 'hard'
                  ? 'bg-rose-100 text-rose-800 border border-rose-200'
                  : pref.preference_type === 'learned'
                  ? 'bg-purple-100 text-purple-800 border border-purple-200'
                  : 'bg-emerald-100 text-emerald-800 border border-emerald-200'
              }`}
            >
              {pref.preference_type.toUpperCase()}
            </span>
            <span className="text-[10px] text-muted font-mono">
              {(pref.confidence * 100).toFixed(0)}% conf
            </span>
          </div>
          <p className="text-sm font-medium text-foreground">{pref.value}</p>
          {pref.raw_query && (
            <p className="text-[11px] text-muted italic">&ldquo;{pref.raw_query}&rdquo;</p>
          )}
        </div>

        <div className="flex items-center gap-1.5 flex-shrink-0">
          {/* Toggle Type button */}
          <button
            onClick={() =>
              onUpdatePreference(pref.id, {
                preference_type: pref.preference_type === 'hard' ? 'soft' : 'hard',
              })
            }
            className="text-xs px-2.5 py-1 rounded-lg border border-neutral-200 hover:bg-neutral-50 text-neutral-600 transition-colors"
            title="Toggle between Hard requirement and Soft preference"
          >
            Make {pref.preference_type === 'hard' ? 'Soft' : 'Hard'}
          </button>

          {/* Delete button */}
          <button
            onClick={() => onDeletePreference(pref.id)}
            className="p-1.5 text-neutral-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
            aria-label="Remove preference"
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </div>
    );
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button
            onClick={onBackToChat}
            className="p-2 border border-neutral-200 rounded-xl hover:bg-neutral-100 text-neutral-700 transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <h1 className="text-xl font-bold text-foreground flex items-center gap-2">
              <SlidersHorizontal className="w-5 h-5 text-amber-600" />
              <span>Understood Preferences</span>
            </h1>
            <p className="text-xs text-muted">
              Everything HeeraMon understands about your career goals and life priorities.
            </p>
          </div>
        </div>

        <button
          onClick={() => setShowAddForm(!showAddForm)}
          className="flex items-center gap-1.5 px-3 py-1.5 bg-neutral-900 text-white rounded-xl text-xs font-medium hover:bg-neutral-800 transition-colors shadow-xs"
        >
          <Plus className="w-3.5 h-3.5" />
          <span>{showAddForm ? 'Cancel' : 'Add Preference'}</span>
        </button>
      </div>

      {/* Add preference inline form */}
      {showAddForm && (
        <form onSubmit={handleAddSubmit} className="bg-white border border-neutral-300 rounded-2xl p-4 shadow-sm space-y-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-neutral-600">Add New Explicit Preference</h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="text-[11px] font-semibold text-neutral-500">Category</label>
              <select
                value={newCategory}
                onChange={(e) => setNewCategory(e.target.value)}
                className="w-full text-xs p-2 border border-neutral-200 rounded-lg bg-neutral-50 mt-1"
              >
                <option value="salary">Salary</option>
                <option value="role">Role / Tech</option>
                <option value="work_arrangement">Work Arrangement</option>
                <option value="commute">Commute Time</option>
                <option value="hours">Workday Hours</option>
                <option value="culture">Culture</option>
                <option value="benefits">Benefits & Lunch</option>
                <option value="location">Location</option>
              </select>
            </div>

            <div>
              <label className="text-[11px] font-semibold text-neutral-500">Value</label>
              <input
                type="text"
                value={newValue}
                onChange={(e) => setNewValue(e.target.value)}
                placeholder="e.g. Min 50,000 BDT or Subsidized lunch"
                className="w-full text-xs p-2 border border-neutral-200 rounded-lg bg-neutral-50 mt-1"
              />
            </div>

            <div>
              <label className="text-[11px] font-semibold text-neutral-500">Requirement Type</label>
              <select
                value={newType}
                onChange={(e) => setNewType(e.target.value as PreferenceType)}
                className="w-full text-xs p-2 border border-neutral-200 rounded-lg bg-neutral-50 mt-1"
              >
                <option value="soft">Soft Preference (Negotiable trade-off)</option>
                <option value="hard">Hard Requirement (Must satisfy)</option>
              </select>
            </div>
          </div>

          <div className="flex justify-end pt-1">
            <button
              type="submit"
              disabled={!newValue.trim()}
              className="px-4 py-1.5 bg-emerald-600 text-white rounded-lg text-xs font-semibold hover:bg-emerald-700 disabled:opacity-50 transition-colors"
            >
              Save to Memory
            </button>
          </div>
        </form>
      )}

      {/* Preferences Sections */}
      <div className="space-y-6">
        {/* 1. Hard Requirements */}
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-rose-600" />
            <h2 className="text-sm font-bold text-foreground">Hard Requirements ({hardPrefs.length})</h2>
            <span className="text-xs text-muted">Mandatory filters. Non-negotiable conditions.</span>
          </div>
          {hardPrefs.length === 0 ? (
            <p className="text-xs text-muted bg-neutral-50 p-3 rounded-xl border border-dashed border-neutral-200">
              No hard requirements established yet. Express conditions like &quot;minimum 40k&quot; or &quot;remote only&quot;.
            </p>
          ) : (
            <div className="grid gap-2.5">{hardPrefs.map(renderPreferenceCard)}</div>
          )}
        </div>

        {/* 2. Soft Preferences */}
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-emerald-600" />
            <h2 className="text-sm font-bold text-foreground">Soft Preferences ({softPrefs.length})</h2>
            <span className="text-xs text-muted">Desirable attributes that allow intelligent trade-offs.</span>
          </div>
          {softPrefs.length === 0 ? (
            <p className="text-xs text-muted bg-neutral-50 p-3 rounded-xl border border-dashed border-neutral-200">
              No soft preferences yet. Mention preferences like &quot;around 7 hours&quot;, &quot;subsidized lunch&quot;, or &quot;friendly culture&quot;.
            </p>
          ) : (
            <div className="grid gap-2.5">{softPrefs.map(renderPreferenceCard)}</div>
          )}
        </div>

        {/* 3. Learned Preferences */}
        {learnedPrefs.length > 0 && (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <Brain className="w-4 h-4 text-purple-600" />
              <h2 className="text-sm font-bold text-foreground">Learned Behavioral Insights ({learnedPrefs.length})</h2>
              <span className="text-xs text-muted">— Inferred from your opportunity decisions.</span>
            </div>
            <div className="grid gap-2.5">{learnedPrefs.map(renderPreferenceCard)}</div>
          </div>
        )}
      </div>

    </div>
  );
};
