'use client';

import React from 'react';
import { Job } from '../types';
import { X, Building2, MapPin, DollarSign, Clock, ExternalLink, FileText, CheckCircle2 } from 'lucide-react';

interface JobDetailModalProps {
  job: Job | null;
  onClose: () => void;
  onPrepareApplication: (jobId: string) => void;
}

export const JobDetailModal: React.FC<JobDetailModalProps> = ({
  job,
  onClose,
  onPrepareApplication,
}) => {
  if (!job) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-neutral-200 rounded-2xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-xl overflow-hidden">
        
        {/* Header */}
        <div className="p-5 border-b border-neutral-200 flex items-start justify-between">
          <div className="space-y-1">
            <h2 className="text-lg font-bold text-foreground">{job.title}</h2>
            <div className="flex items-center gap-3 text-xs text-muted flex-wrap">
              <span className="flex items-center gap-1 font-medium text-neutral-800">
                <Building2 className="w-3.5 h-3.5 text-neutral-500" />
                {job.company}
              </span>
              <span className="flex items-center gap-1">
                <MapPin className="w-3.5 h-3.5 text-neutral-500" />
                {job.location} ({job.work_arrangement})
              </span>
              {job.salary_min && (
                <span className="flex items-center gap-1 font-semibold text-emerald-700">
                  <DollarSign className="w-3.5 h-3.5" />
                  {job.salary_min.toLocaleString()} - {job.salary_max?.toLocaleString()} {job.salary_currency}
                </span>
              )}
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-neutral-400 hover:text-neutral-700 hover:bg-neutral-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable Content */}
        <div className="p-5 overflow-y-auto space-y-5 text-sm">
          {/* Quick Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 bg-neutral-50 p-3.5 rounded-xl border border-neutral-200/80 text-xs">
            <div>
              <span className="text-neutral-500">Commute Time</span>
              <p className="font-semibold text-foreground mt-0.5">
                {job.commute_time_minutes !== null ? `~${job.commute_time_minutes} minutes` : 'Zero (Remote)'}
              </p>
            </div>
            <div>
              <span className="text-neutral-500">Working Day</span>
              <p className="font-semibold text-foreground mt-0.5">
                {job.workday_hours ? `${job.workday_hours} hours/day` : 'Standard ~8h'}
              </p>
            </div>
            <div>
              <span className="text-neutral-500">Employment Type</span>
              <p className="font-semibold text-foreground mt-0.5 capitalize">
                {job.employment_type || 'Full-time'}
              </p>
            </div>
          </div>

          {/* Description */}
          <div className="space-y-1.5">
            <h3 className="text-xs font-bold uppercase tracking-wider text-neutral-500">Role Overview</h3>
            <p className="text-neutral-800 leading-relaxed whitespace-pre-line text-xs sm:text-sm">
              {job.description}
            </p>
          </div>

          {/* Required Skills */}
          {job.required_skills && job.required_skills.length > 0 && (
            <div className="space-y-1.5">
              <h3 className="text-xs font-bold uppercase tracking-wider text-neutral-500">Required Skills & Tech</h3>
              <div className="flex flex-wrap gap-1.5">
                {job.required_skills.map((skill, idx) => (
                  <span
                    key={idx}
                    className="text-xs px-2.5 py-1 bg-neutral-100 text-neutral-800 rounded-lg border border-neutral-200"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Benefits */}
          {job.benefits && job.benefits.length > 0 && (
            <div className="space-y-1.5">
              <h3 className="text-xs font-bold uppercase tracking-wider text-neutral-500">Benefits & Perks</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                {job.benefits.map((benefit, idx) => (
                  <div key={idx} className="flex items-center gap-1.5 text-xs text-neutral-700">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                    <span>{benefit}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Culture Notes */}
          {job.culture_notes && (
            <div className="space-y-1.5 bg-amber-50/50 border border-amber-200/60 p-3 rounded-xl text-xs">
              <h3 className="font-bold text-amber-900">Workplace Culture Insight</h3>
              <p className="text-neutral-800">{job.culture_notes}</p>
            </div>
          )}
        </div>

        {/* Footer Actions */}
        <div className="p-4 border-t border-neutral-200 bg-neutral-50 flex items-center justify-between">
          {job.application_url ? (
            <a
              href={job.application_url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1.5 text-xs text-neutral-600 hover:text-foreground font-medium underline"
            >
              <span>Source Listing</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          ) : <div />}

          <div className="flex items-center gap-2">
            <button
              onClick={onClose}
              className="px-4 py-2 border border-neutral-300 rounded-xl text-xs font-semibold text-neutral-700 hover:bg-neutral-100 transition-colors"
            >
              Close
            </button>
            <button
              onClick={() => {
                onClose();
                onPrepareApplication(job.id);
              }}
              className="flex items-center gap-1.5 px-4 py-2 bg-neutral-900 text-white rounded-xl text-xs font-semibold hover:bg-neutral-800 transition-colors shadow-xs"
            >
              <FileText className="w-3.5 h-3.5" />
              <span>Prepare Application</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
