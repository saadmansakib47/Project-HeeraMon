'use client';

import React from 'react';
import { Match } from '../types';
import { 
  Building2, MapPin, DollarSign, Clock, CheckCircle2, AlertTriangle, 
  HelpCircle, Sparkles, FileText, Bookmark, XCircle, ThumbsUp, ArrowRight
} from 'lucide-react';

interface OpportunitiesViewProps {
  matches: Match[];
  onOpenJobDetail: (jobId: string) => void;
  onPrepareApplication: (jobId: string) => void;
  onRecordDecision: (matchId: string, decision: string) => Promise<void>;
  onBackToChat: () => void;
}

export const OpportunitiesView: React.FC<OpportunitiesViewProps> = ({
  matches,
  onOpenJobDetail,
  onPrepareApplication,
  onRecordDecision,
  onBackToChat,
}) => {
  return (
    <div className="max-w-4xl mx-auto space-y-6">
      
      {/* View Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-foreground flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-amber-500" />
            <span>Opportunities Horizon ({matches.length})</span>
          </h1>
          <p className="text-xs text-muted">
            Ranked opportunities evaluated against your lifestyle and professional criteria.
          </p>
        </div>
      </div>

      {matches.length === 0 ? (
        <div className="bg-white border border-neutral-200 rounded-2xl p-12 text-center space-y-4">
          <p className="text-sm font-semibold text-foreground">No matching opportunities yet</p>
          <p className="text-xs text-muted max-w-sm mx-auto">
            Tell HeeraMon about your target role and requirements in the chat, or trigger a search cycle across sources.
          </p>
          <button
            onClick={onBackToChat}
            className="px-4 py-2 bg-neutral-900 text-white rounded-xl text-xs font-semibold hover:bg-neutral-800 transition-colors"
          >
            Go to Dialogue
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          {matches.map((m) => {
            const job = m.job;
            if (!job) return null;

            return (
              <div
                key={m.id}
                className="bg-white border border-neutral-200 rounded-2xl p-5 shadow-xs hover:shadow-sm transition-all space-y-4"
              >
                {/* Header row */}
                <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
                  <div className="space-y-1">
                    <div className="flex items-center gap-2.5 flex-wrap">
                      <h2 
                        onClick={() => onOpenJobDetail(job.id)}
                        className="text-base font-bold text-foreground hover:text-amber-700 cursor-pointer transition-colors"
                      >
                        {job.title}
                      </h2>
                      <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200 flex items-center gap-1">
                        <Sparkles className="w-3 h-3" />
                        <span>{m.score.toFixed(0)}% Compatibility</span>
                      </span>
                    </div>

                    <div className="flex items-center gap-4 text-xs text-muted flex-wrap">
                      <span className="flex items-center gap-1">
                        <Building2 className="w-3.5 h-3.5" />
                        {job.company}
                      </span>
                      <span className="flex items-center gap-1">
                        <MapPin className="w-3.5 h-3.5" />
                        {job.location} ({job.work_arrangement})
                      </span>
                      {job.salary_min && (
                        <span className="flex items-center gap-1 font-medium text-emerald-700">
                          <DollarSign className="w-3.5 h-3.5" />
                          {job.salary_min.toLocaleString()} {job.salary_currency}
                          {job.salary_max && ` - ${job.salary_max.toLocaleString()} ${job.salary_currency}`}
                        </span>
                      )}
                      {job.workday_hours && (
                        <span className="flex items-center gap-1">
                          <Clock className="w-3.5 h-3.5" />
                          ~{job.workday_hours}h/day
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Primary Action: Prepare Application */}
                  <div className="flex items-center gap-2 flex-shrink-0">
                    <button
                      onClick={() => onPrepareApplication(job.id)}
                      className="flex items-center gap-1.5 px-3.5 py-1.5 bg-neutral-900 hover:bg-neutral-800 text-white rounded-xl text-xs font-semibold shadow-xs transition-colors"
                    >
                      <FileText className="w-3.5 h-3.5" />
                      <span>Prepare Application</span>
                    </button>
                  </div>
                </div>

                {/* HeeraMon Reasoning Explanation */}
                {m.explanation && (
                  <div className="bg-amber-50/60 border border-amber-200/80 rounded-xl p-3 text-xs text-neutral-800 leading-relaxed">
                    <span className="font-semibold text-amber-900">HeeraMon&apos;s Advice: </span>
                    {m.explanation}
                  </div>
                )}

                {/* Structured Breakdown Chips */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                  {/* Satisfied */}
                  {m.satisfied_preferences.length > 0 && (
                    <div className="space-y-1 bg-emerald-50/50 border border-emerald-100 p-2.5 rounded-xl">
                      <span className="text-[11px] font-bold text-emerald-800 flex items-center gap-1">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                        Satisfied Priorities ({m.satisfied_preferences.length})
                      </span>
                      <ul className="space-y-0.5 text-neutral-700 pl-4 list-disc text-[11px]">
                        {m.satisfied_preferences.map((s, idx) => (
                          <li key={idx}>{s}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Trade-offs / Violated */}
                  {(m.trade_offs.length > 0 || m.violated_preferences.length > 0) && (
                    <div className="space-y-1 bg-amber-50/50 border border-amber-200/70 p-2.5 rounded-xl">
                      <span className="text-[11px] font-bold text-amber-800 flex items-center gap-1">
                        <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                        Trade-offs & Differences
                      </span>
                      <ul className="space-y-0.5 text-neutral-700 pl-4 list-disc text-[11px]">
                        {[...m.trade_offs, ...m.violated_preferences].map((t, idx) => (
                          <li key={idx}>{t}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>

                {/* Footer Decision Buttons */}
                <div className="pt-2 border-t border-neutral-100 flex items-center justify-between text-xs">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => onRecordDecision(m.id, 'interested')}
                      className="flex items-center gap-1 px-2.5 py-1 rounded-lg border border-neutral-200 hover:bg-emerald-50 hover:text-emerald-700 text-neutral-600 transition-colors"
                    >
                      <ThumbsUp className="w-3 h-3" />
                      <span>Interested</span>
                    </button>

                    <button
                      onClick={() => onRecordDecision(m.id, 'saved')}
                      className="flex items-center gap-1 px-2.5 py-1 rounded-lg border border-neutral-200 hover:bg-neutral-100 text-neutral-600 transition-colors"
                    >
                      <Bookmark className="w-3 h-3" />
                      <span>Save</span>
                    </button>

                    <button
                      onClick={() => onRecordDecision(m.id, 'rejected')}
                      className="flex items-center gap-1 px-2.5 py-1 rounded-lg border border-neutral-200 hover:bg-rose-50 hover:text-rose-700 text-neutral-600 transition-colors"
                    >
                      <XCircle className="w-3 h-3" />
                      <span>Decline</span>
                    </button>
                  </div>

                  <button
                    onClick={() => onOpenJobDetail(job.id)}
                    className="flex items-center gap-1 text-neutral-600 hover:text-foreground font-medium transition-colors"
                  >
                    <span>Full Details</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>

              </div>
            );
          })}
        </div>
      )}

    </div>
  );
};
