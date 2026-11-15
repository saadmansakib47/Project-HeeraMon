export type PreferenceType = 'hard' | 'soft' | 'learned' | 'unknown';
export type PreferenceSource = 'explicit' | 'confirmed' | 'inferred';

export interface UserPreference {
  id: string;
  user_id: string;
  category: string;
  value: string;
  preference_type: PreferenceType;
  source: PreferenceSource;
  confidence: number;
  status: string;
  raw_query?: string;
  created_at: string;
  updated_at: string;
}

export interface Job {
  id: string;
  title: string;
  company: string;
  description: string;
  location: string;
  work_arrangement: 'remote' | 'hybrid' | 'onsite';
  employment_type?: string;
  salary_min?: number;
  salary_max?: number;
  salary_currency?: string;
  commute_time_minutes?: number;
  workday_hours?: number;
  required_skills?: string[];
  benefits?: string[];
  culture_notes?: string;
  application_url?: string;
  status: string;
  first_seen_at: string;
  last_seen_at: string;
}

export interface Match {
  id: string;
  user_id: string;
  job_id: string;
  score: number;
  eligibility_status: 'eligible' | 'ineligible' | 'review';
  satisfied_preferences: string[];
  violated_preferences: string[];
  unknown_information: string[];
  trade_offs: string[];
  explanation: string;
  job?: Job;
  created_at: string;
  updated_at: string;
}

export interface Message {
  id: string;
  conversation_id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  metadata_info?: {
    extracted_count?: number;
    suggested_chips?: string[];
    matches_count?: number;
  };
  timestamp: string;
}

export interface Conversation {
  id: string;
  user_id: string;
  title: string;
  messages: Message[];
  created_at: string;
  updated_at: string;
}

export interface User {
  id: string;
  email: string;
  name: string;
  profile_data?: Record<string, any>;
  created_at: string;
  updated_at: string;
}

export interface Application {
  id: string;
  user_id: string;
  job_id: string;
  status: 'draft' | 'review' | 'approved' | 'submitted' | 'cancelled';
  tailored_notes?: string;
  cover_letter?: string;
  submission_data?: Record<string, any>;
  submitted_at?: string;
  job?: Job;
  created_at: string;
  updated_at: string;
}

export interface AppNotification {
  id: string;
  user_id: string;
  notification_type: 'new_match' | 'preference_suggestion' | 'alert';
  title: string;
  content: string;
  related_job_id?: string;
  is_read: boolean;
  created_at: string;
}

export interface ChatResponse {
  conversation_id: string;
  message: Message;
  extracted_preferences: UserPreference[];
  matched_jobs: Match[];
  suggested_chips: string[];
}
