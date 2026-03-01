/**
 * KiriMel Node.js SDK
 *
 * Official Node.js SDK for KiriMel Email Marketing API.
 */
export { Client } from './client';
export { HttpClient } from './httpClient';
export {
  ApiException,
  AuthenticationException,
  RateLimitException,
  ValidationException,
} from './exceptions';
export type { Logger, HttpClientConfig } from './httpClient';
export type { ClientConfig } from './client';
