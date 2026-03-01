/**
 * Segments resource client
 */
import { HttpClient } from '../httpClient';

export class Segments {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(listId: number): Promise<any> {
    return this.httpClient.get(`lists/${listId}/segments`);
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`segments/${id}`);
  }

  public async create(listId: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`lists/${listId}/segments`, data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`segments/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`segments/${id}/delete`);
  }

  public async preview(listId: number, conditions: any[]): Promise<any> {
    return this.httpClient.post(`lists/${listId}/segments/preview`, { conditions });
  }

  public async subscribers(id: number, params?: Record<string, any>): Promise<any> {
    return this.httpClient.get(`segments/${id}/subscribers`, params);
  }

  public async refresh(id: number): Promise<any> {
    return this.httpClient.post(`segments/${id}/refresh`);
  }

  public async logs(id: number): Promise<any> {
    return this.httpClient.get(`segments/${id}/logs`);
  }

  public async templates(): Promise<any> {
    return this.httpClient.get('segments/templates');
  }

  public async fields(): Promise<any> {
    return this.httpClient.get('segments/fields');
  }
}
