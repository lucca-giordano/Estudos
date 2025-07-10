import { eq } from 'drizzle-orm';
import type { FastifyPluginCallbackZod } from 'fastify-type-provider-zod';
import { z } from 'zod/v4';
import { db } from '../../db/connection.ts';
import { schema } from '../../db/schema/index.ts';

export const getRoomQuestions: FastifyPluginCallbackZod = (app) => {
  app.get(
    '/rooms/:roomId/questions',
    {
      schema: {
        params: z.object({
          roomId: z.string(),
        }),
      },
    },
    async (request) => {
      const { roomId } = request.params;

      const result = await db
        .select({
            id: schema.questions.id,
            question: schema.questions.question,
            answer: schema.questions.answer,
            createdAt: schema.questions.createdAt
        })
        .from(schema.questions)
        .leftJoin(schema.questions, eq(schema.questions.roomId, schema.rooms.id))
        .where(eq(schema.questions.roomId, roomId))
        .orderBy(schema.questions.createdAt);

        return result
    }
  );
};
