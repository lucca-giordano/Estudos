import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { CreateRoom } from './pages/create-room';
import { Room } from './pages/room';

const queryClient = new QueryClient()

export function App() {
  return (
    <div>
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <Routes>
            <Route element={<CreateRoom />} index />
            <Route element={<Room />} path="/room/:roomId" />
          </Routes>
        </BrowserRouter>
      </QueryClientProvider>
    </div>
  );
}
