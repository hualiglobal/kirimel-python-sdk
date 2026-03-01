/**
 * Forms resource client
 */
import { HttpClient } from '../httpClient';

export class Forms {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(): Promise<any> {
    return this.httpClient.get('forms');
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`forms/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('forms', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`forms/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`forms/${id}/delete`);
  }

  public async duplicate(id: number): Promise<any> {
    return this.httpClient.post(`forms/${id}/duplicate`);
  }

  public async analytics(id: number): Promise<any> {
    return this.httpClient.get(`forms/${id}/analytics`);
  }

  public async submissions(id: number, params?: Record<string, any>): Promise<any> {
    return this.httpClient.get(`forms/${id}/submissions`, params);
  }

  public async embed(id: number): Promise<any> {
    return this.httpClient.get(`forms/${id}/embed`);
  }
}
