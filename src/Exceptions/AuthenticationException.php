<?php

declare(strict_types=1);

namespace KiriMel\Exceptions;

/**
 * Authentication exception (401)
 */
class AuthenticationException extends ApiException
{
    protected ?string $errorType = 'authentication_error';
}
