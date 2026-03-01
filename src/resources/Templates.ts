/**
 * Templates resource client
 */
import { HttpClient } from '../httpClient';

export class Templates {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(params?: Record<string, any>): Promise<any> {
    return this.httpClient.get('templates', params);
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`templates/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('templates', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`templates/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`templates/${id}/delete`);
  }

  public async duplicate(id: number): Promise<any> {
    return this.httpClient.post(`templates/${id}/duplicate`);
  }

  public async byCategory(category: string): Promise<any> {
    return this.httpClient.get(`templates/category/${category}`);
  }

  public async search(query: string): Promise<any> {
    return this.httpClient.get('templates/search', { q: query });
  }

  public async categories(): Promise<any> {
    return this.httpClient.get('templates/categories');
  }
}
