import Navbar from '@/components/Navbar';
import ChatView from '@/components/ChatView';

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-1 p-4">
        <ChatView />
      </main>
    </div>
  );
}
