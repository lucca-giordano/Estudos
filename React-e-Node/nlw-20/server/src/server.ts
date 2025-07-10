import { fastifyCors } from '@fastify/cors';
import { fastify } from 'fastify';
import {
  serializerCompiler,
  validatorCompiler,
  type ZodTypeProvider,
} from 'fastify-type-provider-zod';
import { env } from './env.ts';
import { createQuestionRoute } from './http/routes/create-question.ts';
import { createRoomsRoute } from './http/routes/create-rooms.ts';
import { getRoomQuestions } from './http/routes/get-room-questions.ts';
import { getRoomsRoute } from './http/routes/get-rooms.ts';

const app = fastify().withTypeProvider<ZodTypeProvider>();

app.register(fastifyCors, {
  origin: 'http://localhost:5173',
});

app.setSerializerCompiler(serializerCompiler);
app.setValidatorCompiler(validatorCompiler);

app.get('/health', () => {
  return { status: 'ok' };
});

app.register(getRoomsRoute);
app.register(createRoomsRoute);
app.register(getRoomQuestions);
app.register(createQuestionRoute);

app.listen({ port: env.PORT }).then(() => {
  app.log.info(`HTTP server running on port ${env.PORT}`);
  app.log.info(`Access the app at http://localhost:${env.PORT}`);
});
