/**
 * KiriMel SDK Exception Classes
 */

export interface ApiError {
  message: string;
  field?: string;
}

export class ApiException extends Error {
  public readonly statusCode?: number;
  public readonly errors?: ApiError[];
  public readonly errorType?: string;

  constructor(
    message: string,
    statusCode?: number,
    errors?: ApiError[]
  ) {
    super(message);
    this.name = 'ApiException';
    this.statusCode = statusCode;
    this.errors = errors;
  }
}

export class AuthenticationException extends ApiException {
  public readonly errorType = 'authentication_error';

  constructor(message: string, statusCode?: number, errors?: ApiError[]) {
    super(message, statusCode, errors);
    this.name = 'AuthenticationException';
  }
}

export class RateLimitException extends ApiException {
  public readonly errorType = 'rate_limit_error';
  public readonly retryAfter?: number;

  constructor(
    message: string,
    statusCode?: number,
    errors?: ApiError[],
    retryAfter?: number
  ) {
    super(message, statusCode, errors);
    this.name = 'RateLimitException';
    this.retryAfter = retryAfter;
  }
}

export class ValidationException extends ApiException {
  public readonly errorType = 'validation_error';

  constructor(message: string, statusCode?: number, errors?: ApiError[]) {
    super(message, statusCode, errors);
    this.name = 'ValidationException';
  }
}
