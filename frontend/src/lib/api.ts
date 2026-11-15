import { 
  User, UserPreference, Conversation, Match, Job, Application, AppNotification, ChatResponse 
} from '../types';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

async function fetchJSON<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  });

  if (!res.ok) {
    const errorText = await res.text();
    throw new Error(`API Error [${res.status}]: ${errorText}`);
  }

  return res.json();
}

export const api = {
  // Auth & Profile
  getCurrentUser: () => fetchJSON<User>('/auth/me'),

  // Conversations
  getConversations: () => fetchJSON<Conversation[]>('/conversations'),
  getConversation: (id: string) => fetchJSON<Conversation>(`/conversations/${id}`),
  sendMessage: (conversationId: string, content: string) =>
    fetchJSON<ChatResponse>(`/conversations/${conversationId}/messages`, {
      method: 'POST',
      body: JSON.stringify({ content }),
    }),

  // Preferences
  getPreferences: () => fetchJSON<UserPreference[]>('/preferences'),
  createPreference: (pref: Partial<UserPreference>) =>
    fetchJSON<UserPreference>('/preferences', {
      method: 'POST',
      body: JSON.stringify(pref),
    }),
  updatePreference: (id: string, updates: Partial<UserPreference>) =>
    fetchJSON<UserPreference>(`/preferences/${id}`, {
      method: 'PATCH',
      body: JSON.stringify(updates),
    }),
  deletePreference: (id: string) =>
    fetchJSON<{ message: string }>(`/preferences/${id}`, {
      method: 'DELETE',
    }),

  // Jobs & Matches
  getJobs: () => fetchJSON<Job[]>('/jobs'),
  getJob: (id: string) => fetchJSON<Job>(`/jobs/${id}`),
  getMatches: () => fetchJSON<Match[]>('/matches'),
  getMatch: (id: string) => fetchJSON<Match>(`/matches/${id}`),
  recordDecision: (matchId: string, decision: string, reason?: string) =>
    fetchJSON<{ status: string; decision: string }>(`/matches/${matchId}/decision`, {
      method: 'POST',
      body: JSON.stringify({ decision, reason }),
    }),

  // Continuous Search & Ingestion
  triggerIngestion: () => fetchJSON<{ status: string; stats: any }>('/jobs/ingest', { method: 'POST' }),
  triggerBackgroundSearch: () =>
    fetchJSON<{ status: string; summary: any }>('/notifications/trigger-background-search', {
      method: 'POST',
    }),

  // Notifications
  getNotifications: () => fetchJSON<AppNotification[]>('/notifications'),
  markNotificationRead: (id: string) =>
    fetchJSON<{ status: string; id: string }>(`/notifications/${id}/read`, {
      method: 'PATCH',
    }),

  // Applications
  getApplications: () => fetchJSON<Application[]>('/applications'),
  prepareApplication: (jobId: string) =>
    fetchJSON<Application>('/applications/prepare', {
      method: 'POST',
      body: JSON.stringify({ job_id: jobId }),
    }),
  approveApplication: (appId: string) =>
    fetchJSON<Application>(`/applications/${appId}/approve`, {
      method: 'POST',
      body: JSON.stringify({ confirm_submission: true }),
    }),
};
