import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';

type GetRoomsAPIResponse = Array<{
  id: string;
  name: string;
}>;

export function CreateRoom() {
  const { data, isLoading } = useQuery({
    queryKey: ['get-rooms'],
    queryFn: async () => {
      const response = await fetch('/rooms');
      const result: GetRoomsAPIResponse = await response.json();

      return result;
    },
  });

  return (
    <div>
      <div>Create room</div>

      {isLoading && <p>Carregando...</p>}
      <div className="flex flex-col gap-1">
        {data?.map((room) => {
          return (
            <Link className="underline" key={room.id} to={`/room/${room.id}`}>
              {room.name}
            </Link>
          );
        })}
      </div>

      <Link className="underline" to="/room">
        Room details
      </Link>
    </div>
  );
}
