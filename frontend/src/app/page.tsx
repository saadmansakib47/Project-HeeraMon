import React, { useEffect } from 'react';
import Navbar from '@/components/Navbar';
import ChatView from '@/components/ChatView';
import { api } from '@/lib/api';
import { useHeeraMon } from '@/context/HeeraMonContext';
import ChatView from '@/components/ChatView';

export default function HomePage() {
  const { user, conversation, messages, preferences, jobs, setUser, setConversation, setMessages, setPreferences, setJobs } = useHeeraMon();
  const [activeTab, setActiveTab] = React.useState<'chat' | 'opportunities' | 'preferences'>('chat');
  const [isSearching, setIsSearching] = React.useState(false);
  const [matchesCount, setMatchesCount] = React.useState(0);
  const [preferencesCount, setPreferencesCount] = React.useState(0);
  const [unreadNotificationsCount, setUnreadNotificationsCount] = React.useState(0);

  // Load initial data on mount
  React.useEffect(() => {
    // Fetch current user & default conversation
    api.getCurrentUser().then(setUser).catch(console.error);
    api.getConversations().then((convs) => {
      if (convs.length) {
        setConversation(convs[0]);
        api.getConversation(convs[0].id).then((conv) => setMessages(conv.messages)).catch(console.error);
      }
    }).catch(console.error);
    // Preferences count
    api.getPreferences().then((prefs) => { setPreferences(prefs); setPreferencesCount(prefs.length); }).catch(console.error);
    // Jobs / matches count (placeholder)
    api.getMatches().then((matches) => setMatchesCount(matches.length)).catch(console.error);
    // Notifications count
    api.getNotifications().then((notes) => {
      const unread = notes.filter((n) => !n.read).length;
      setUnreadNotificationsCount(unread);
    }).catch(console.error);
  }, []);

  const handleOpenNotifications = () => {
    // For now just clear the badge
    setUnreadNotificationsCount(0);
  };

  const handleTriggerSearch = async () => {
    setIsSearching(true);
    try {
      await api.triggerBackgroundSearch();
      // could refresh matches later
    } catch (e) {
      console.error(e);
    } finally {
      setIsSearching(false);
    }
  };

  const handleSendMessage = async (content: string) => {
    if (!conversation) return;
    const resp = await api.sendMessage(conversation.id, content);
    // Append new messages and update matches if any
    setMessages((prev) => [...prev, ...resp.messages]);
    if (resp.matches) {
      setMatchesCount((c) => c + resp.matches.length);
    }
  };
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-1 p-4">
        <ChatView />
      </main>
    </div>
  );
}
