/**
 * Campaigns resource client
 */
import { HttpClient } from '../httpClient';

export class Campaigns {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(params?: Record<string, any>): Promise<any> {
    return this.httpClient.get('campaigns', params);
  }

  public async recent(): Promise<any> {
    return this.httpClient.get('campaigns/recent');
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`campaigns/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('campaigns', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`campaigns/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`campaigns/${id}/delete`);
  }

  public async duplicate(id: number): Promise<any> {
    return this.httpClient.post(`campaigns/${id}/duplicate`);
  }

  public async schedule(id: number, scheduledAt: string): Promise<any> {
    return this.httpClient.post(`campaigns/${id}/schedule`, { scheduled_at: scheduledAt });
  }

  public async pause(id: number): Promise<any> {
    return this.httpClient.post(`campaigns/${id}/pause`);
  }

  public async resume(id: number): Promise<any> {
    return this.httpClient.post(`campaigns/${id}/resume`);
  }

  public async stats(id: number): Promise<any> {
    return this.httpClient.get(`campaigns/${id}/stats`);
  }
}
