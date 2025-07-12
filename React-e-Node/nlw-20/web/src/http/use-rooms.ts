import { useQuery } from "@tanstack/react-query";
import type { GetRoomsAPIResponse } from "./types/get-rooms-response";

export function useRooms() {
      return useQuery({
        queryKey: ['get-rooms'],
        queryFn: async () => {
          const response = await fetch('/rooms');
          const result: GetRoomsAPIResponse = await response.json();

          return result;
        },
      });
}