/**
 * Workflows resource client
 */
import { HttpClient } from '../httpClient';

export class Workflows {
  constructor(private readonly httpClient: HttpClient) {}

  public async list(): Promise<any> {
    return this.httpClient.get('workflows');
  }

  public async get(id: number): Promise<any> {
    return this.httpClient.get(`workflows/${id}`);
  }

  public async create(data: Record<string, any>): Promise<any> {
    return this.httpClient.post('workflows', data);
  }

  public async update(id: number, data: Record<string, any>): Promise<any> {
    return this.httpClient.post(`workflows/${id}`, data);
  }

  public async delete(id: number): Promise<any> {
    return this.httpClient.post(`workflows/${id}/delete`);
  }

  public async duplicate(id: number): Promise<any> {
    return this.httpClient.post(`workflows/${id}/duplicate`);
  }

  public async activate(id: number): Promise<any> {
    return this.httpClient.post(`workflows/${id}/activate`);
  }

  public async pause(id: number): Promise<any> {
    return this.httpClient.post(`workflows/${id}/pause`);
  }

  public async validate(id: number): Promise<any> {
    return this.httpClient.post(`workflows/${id}/validate`);
  }

  public async executions(id: number): Promise<any> {
    return this.httpClient.get(`workflows/${id}/executions`);
  }

  public async templates(): Promise<any> {
    return this.httpClient.get('workflows/templates');
  }

  public async fromTemplate(templateId: number): Promise<any> {
    return this.httpClient.post('workflows/from-template', { template_id: templateId });
  }

  public async nodeTypes(): Promise<any> {
    return this.httpClient.get('workflows/node-types');
  }

  public async getData(id: number): Promise<any> {
    return this.httpClient.get(`workflows/${id}/data`);
  }
}
