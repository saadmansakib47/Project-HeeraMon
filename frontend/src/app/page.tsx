'use client';
import React, { useEffect } from 'react';
import { Navbar } from '@/components/Navbar';
import { ChatView } from '@/components/ChatView';
import { api } from '@/lib/api';
import { useHeeraMon } from '@/context/HeeraMonContext';

export default function HomePage() {
  const {
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
  } = useHeeraMon();

  const [activeTab, setActiveTab] = React.useState<'chat' | 'opportunities' | 'preferences'>('chat');
  const [isSearching, setIsSearching] = React.useState(false);
  const [matchesCount, setMatchesCount] = React.useState(0);
  const [preferencesCount, setPreferencesCount] = React.useState(0);
  const [unreadNotificationsCount, setUnreadNotificationsCount] = React.useState(0);
  const [suggestedChips, setSuggestedChips] = React.useState<string[]>([]);
  const [recentMatches, setRecentMatches] = React.useState<any[]>([]);

  // Load initial data on mount
  useEffect(() => {
    api.getCurrentUser().then(setUser).catch(console.error);
    api.getConversations()
      .then((convs) => {
        if (convs.length) {
          setConversation(convs[0]);
          api.getConversation(convs[0].id).then((conv) => setMessages(conv.messages)).catch(console.error);
        }
      })
      .catch(console.error);
    api.getPreferences()
      .then((prefs) => {
        setPreferences(prefs);
        setPreferencesCount(prefs.length);
      })
      .catch(console.error);
    api.getMatches()
      .then((matches) => {
        setMatchesCount(matches.length);
        setRecentMatches(matches.slice(0, 5));
      })
      .catch(console.error);
    api.getNotifications()
      .then((notes) => {
        const unread = notes.filter((n) => !n.read).length;
        setUnreadNotificationsCount(unread);
      })
      .catch(console.error);
  }, []);

  const handleOpenNotifications = () => setUnreadNotificationsCount(0);

  const handleTriggerSearch = async () => {
    setIsSearching(true);
    try {
      await api.triggerBackgroundSearch();
    } catch (e) {
      console.error(e);
    } finally {
      setIsSearching(false);
    }
  };

  const handleSendMessage = async (content: string) => {
    if (!conversation) return;
    const resp = await api.sendMessage(conversation.id, content);
    setMessages((prev) => [...prev, ...resp.messages]);
    if (resp.matches) {
      setMatchesCount((c) => c + resp.matches.length);
      setRecentMatches((prev) => [...resp.matches, ...prev].slice(0, 5));
    }
    if (resp.suggested_chips) setSuggestedChips(resp.suggested_chips);
  };

  const handleSelectJob = (jobId: string) => {
    console.log('selected job', jobId);
  };

  const handleOpenPreferences = () => {
    console.log('open preferences');
  };

  return (
    <div className="flex flex-col min-h-screen">
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        matchesCount={matchesCount}
        preferencesCount={preferencesCount}
        unreadNotificationsCount={unreadNotificationsCount}
        onOpenNotifications={handleOpenNotifications}
        onTriggerSearch={handleTriggerSearch}
        isSearching={isSearching}
      />
      <main className="flex-1 p-4">
        <ChatView
          messages={messages}
          isLoading={isSearching}
          suggestedChips={suggestedChips}
          recentMatches={recentMatches}
          onSelectJob={handleSelectJob}
          onOpenPreferences={handleOpenPreferences}
          onSendMessage={handleSendMessage}
        />
      </main>
    </div>
  );
}
