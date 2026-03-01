/**
 * Landing Pages resource client
 */
import { HttpClient } from '../httpClient';

export class LandingPages {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(): Promise<any> {
    return this.httpClient.get('landing-pages');
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`landing-pages/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('landing-pages', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`landing-pages/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`landing-pages/${id}/delete`);
  }

  public async duplicate(id: number): Promise<any> {
    return this.httpClient.post(`landing-pages/${id}/duplicate`);
  }

  public async publish(id: number): Promise<any> {
    return this.httpClient.post(`landing-pages/${id}/publish`);
  }

  public async unpublish(id: number): Promise<any> {
    return this.httpClient.post(`landing-pages/${id}/unpublish`);
  }

  public async analytics(id: number): Promise<any> {
    return this.httpClient.get(`landing-pages/${id}/analytics`);
  }

  public async templates(): Promise<any> {
    return this.httpClient.get('landing-pages/templates');
  }
}
