/**
 * Conversions resource client
 */
import { HttpClient } from '../httpClient';

export class Conversions {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(): Promise<any> {
    return this.httpClient.get('conversions');
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`conversions/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('conversions', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`conversions/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`conversions/${id}/delete`);
  }

  public async track(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('conversions/track', data);
  }

  public async conversions(id: number): Promise<any> {
    return this.httpClient.get(`conversions/${id}/conversions`);
  }

  public async roi(): Promise<any> {
    return this.httpClient.get('conversions/roi');
  }

  public async funnel(id: number): Promise<any> {
    return this.httpClient.get(`conversions/${id}/funnel`);
  }
}
