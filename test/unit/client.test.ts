/**
 * Unit tests for KiriMel Node.js SDK
 */
import { Client } from '../../src/client';

describe('Client', () => {
  let client: Client;

  beforeEach(() => {
    client = new Client({ apiKey: 'test_key' });
  });

  test('should instantiate client', () => {
    expect(client).toBeInstanceOf(Client);
  });

  test('should have campaigns resource', () => {
    expect(client.campaigns).toBeDefined();
  });

  test('should have subscribers resource', () => {
    expect(client.subscribers).toBeDefined();
  });

  test('should have lists resource', () => {
    expect(client.lists).toBeDefined();
  });

  test('should have segments resource', () => {
    expect(client.segments).toBeDefined();
  });

  test('should have templates resource', () => {
    expect(client.templates).toBeDefined();
  });

  test('should have forms resource', () => {
    expect(client.forms).toBeDefined();
  });

  test('should have conversions resource', () => {
    expect(client.conversions).toBeDefined();
  });

  test('should have landingPages resource', () => {
    expect(client.landingPages).toBeDefined();
  });

  test('should have workflows resource', () => {
    expect(client.workflows).toBeDefined();
  });
});
