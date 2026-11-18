'use client';

import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import Image from 'next/image';
import { Send, Sparkles, User as UserIcon, ArrowRight, CheckCircle2, AlertCircle } from 'lucide-react';
import { Message, Match } from '../types';

interface ChatViewProps {
  messages: Message[];
  onSendMessage: (text: string) => Promise<void>;
  isLoading: boolean;
  suggestedChips: string[];
  recentMatches: Match[];
  onSelectJob: (jobId: string) => void;
  onOpenPreferences: () => void;
}

export const ChatView: React.FC<ChatViewProps> = ({
  messages,
  onSendMessage,
  isLoading,
  suggestedChips,
  recentMatches,
  onSelectJob,
  onOpenPreferences,
}) => {
  const [inputText, setInputText] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim() || isLoading) return;
    const text = inputText;
    setInputText('');
    await onSendMessage(text);
  };

  const handleChipClick = async (chip: string) => {
    if (isLoading) return;
    await onSendMessage(chip);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-12rem)] max-w-4xl mx-auto bg-surface border border-border rounded-2xl shadow-sm overflow-hidden font-nunito">
      
      {/* Messages Scroll Area */}
      <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-5">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center p-6 space-y-4">
            <div className="relative w-20 h-20 rounded-full border-2 border-amber-300 p-2 bg-gradient-to-tr from-amber-50 to-emerald-50 shadow-md">
              <Image
                src="/images/HeeraMon-Transparent.png"
                alt="HeeraMon"
                width={80}
                height={80}
                className="object-contain"
              />
            </div>
            <div className="max-w-md space-y-2">
              <h2 className="text-xl font-bold text-foreground">Speak with HeeraMon</h2>
              <p className="text-sm text-muted">
                Describe the work you want and the life you wish to protect. HeeraMon listens to requirements and lifestyle balance alike.
              </p>
            </div>
            <div className="flex flex-wrap justify-center gap-2 pt-2">
              {[
                "At least 40k BDT, AI/ML role, max 30-min commute, subsidized lunch",
                "Remote Python Backend, ~7 hours/day, friendly culture",
                "Full Stack Developer in Dhaka, min 45k, growth-oriented"
              ].map((example, idx) => (
                <button
                  key={idx}
                  onClick={() => handleChipClick(example)}
                  className="text-xs bg-neutral-100 hover:bg-amber-50 text-neutral-700 hover:text-amber-900 border border-neutral-200 hover:border-amber-300 px-3 py-1.5 rounded-full transition-all text-left"
                >
                  &ldquo;{example}&rdquo;
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex gap-3.5 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              {msg.role === 'assistant' && (
                <div className="relative w-9 h-9 rounded-full bg-gradient-to-br from-amber-50 to-emerald-50 border border-amber-300 shadow-sm flex items-center justify-center flex-shrink-0 mt-0.5 overflow-hidden">
                  <Image
                    src="/images/HeeraMon-Transparent.png"
                    alt="HeeraMon"
                    width={32}
                    height={32}
                    className="object-contain"
                  />
                </div>
              )}

              <div
                className={`max-w-[85%] sm:max-w-[78%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-xs ${
                  msg.role === 'user'
                    ? 'bg-neutral-900 text-white rounded-br-none'
                    : 'bg-neutral-50 text-neutral-800 border border-neutral-200/90 rounded-bl-none'
                }`}
              >
                <ReactMarkdown className="whitespace-pre-wrap">{msg.content}</ReactMarkdown>

                {/* Inline job match preview if attached to assistant message */}
                {msg.role === 'assistant' && recentMatches.length > 0 && (
                  <div className="mt-3.5 pt-3 border-t border-neutral-200 space-y-2">
                    <p className="text-xs font-semibold text-neutral-500 uppercase tracking-wider">
                      Discovered Opportunities
                    </p>
                    <div className="grid gap-2">
                      {recentMatches.slice(0, 2).map((m) => (
                        <div
                          key={m.id}
                          onClick={() => onSelectJob(m.job_id)}
                          className="bg-white p-2.5 rounded-xl border border-neutral-200 hover:border-amber-400 hover:shadow-xs transition-all cursor-pointer flex items-center justify-between"
                        >
                          <div>
                            <div className="font-semibold text-xs text-foreground flex items-center gap-1.5">
                              <span>{m.job?.title}</span>
                              <span className="text-[10px] px-1.5 py-0.2 bg-emerald-100 text-emerald-800 rounded font-bold">
                                {m.score.toFixed(0)}% fit
                              </span>
                            </div>
                            <p className="text-[11px] text-muted">{m.job?.company} • {m.job?.location}</p>
                          </div>
                          <ArrowRight className="w-4 h-4 text-neutral-400" />
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {msg.role === 'user' && (
                <div className="w-9 h-9 rounded-full bg-neutral-800 text-white flex items-center justify-center flex-shrink-0 mt-0.5 text-xs font-bold">
                  <UserIcon className="w-4 h-4" />
                </div>
              )}
            </div>
          ))
        )}

        {isLoading && (
          <div className="flex gap-3 items-center text-xs text-muted italic pl-1">
            <div className="w-8 h-8 rounded-full bg-amber-50 border border-amber-200 flex items-center justify-center animate-pulse">
              <Sparkles className="w-4 h-4 text-amber-600 animate-spin" />
            </div>
            <span>HeeraMon is weighing preferences and consulting sources...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Suggestion Chips */}
      {suggestedChips.length > 0 && (
        <div className="px-4 py-2 bg-neutral-50/70 border-t border-border flex items-center gap-2 overflow-x-auto no-scrollbar">
          <span className="text-[11px] font-semibold text-neutral-400 uppercase flex-shrink-0">
            Suggested:
          </span>
          {suggestedChips.map((chip, idx) => (
            <button
              key={idx}
              onClick={() => handleChipClick(chip)}
              disabled={isLoading}
              className="text-xs bg-white text-neutral-700 hover:text-foreground border border-neutral-200 hover:border-amber-300 px-3 py-1 rounded-full whitespace-nowrap transition-colors flex-shrink-0 disabled:opacity-50"
            >
              {chip}
            </button>
          ))}
        </div>
      )}

      {/* Input bar */}
      <form onSubmit={handleSubmit} className="p-3 bg-white border-t border-border flex items-center gap-2">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Speak your mind (salary, tech role, commute, hours, culture...)"
          className="flex-1 px-4 py-2.5 text-sm bg-neutral-50 border border-neutral-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-neutral-900 focus:bg-white transition-all placeholder:text-neutral-400"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={!inputText.trim() || isLoading}
          className="p-2.5 bg-neutral-900 text-white rounded-xl hover:bg-neutral-800 disabled:opacity-40 disabled:hover:bg-neutral-900 transition-colors shadow-xs"
          aria-label="Send message"
        >
          <Send className="w-4 h-4" />
        </button>
      </form>

    </div>
  );
};
