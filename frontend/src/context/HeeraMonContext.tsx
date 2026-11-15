import React, { createContext, useContext, useState, ReactNode } from 'react';
import type { Preference, Conversation, Job, Message, User } from '@/types';

interface HeeraMonState {
  user: User | null;
  conversation: Conversation | null;
  messages: Message[];
  preferences: Preference[];
  jobs: Job[];
}

interface HeeraMonContextProps extends HeeraMonState {
  setUser: (user: User | null) => void;
  setConversation: (conv: Conversation | null) => void;
  setMessages: (msgs: Message[]) => void;
  setPreferences: (prefs: Preference[]) => void;
  setJobs: (jobs: Job[]) => void;
}

const HeeraMonContext = createContext<HeeraMonContextProps | undefined>(undefined);

export const HeeraMonProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [conversation, setConversation] = useState<Conversation | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [preferences, setPreferences] = useState<Preference[]>([]);
  const [jobs, setJobs] = useState<Job[]>([]);

  return (
    <HeeraMonContext.Provider
      value={{
        user,
        conversation,
        messages,
        preferences,
        jobs,
        setUser,
        setConversation,
        setMessages,
        setPreferences,
        setJobs,
      }}
    >
      {children}
    </HeeraMonContext.Provider>
  );
};

export const useHeeraMon = (): HeeraMonContextProps => {
  const context = useContext(HeeraMonContext);
  if (!context) {
    throw new Error('useHeeraMon must be used within a HeeraMonProvider');
  }
  return context;
};
