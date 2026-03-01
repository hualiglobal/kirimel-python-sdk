<?php

declare(strict_types=1);

namespace KiriMel\Tests;

use KiriMel\Client;
use KiriMel\Exceptions\AuthenticationException;
use KiriMel\Exceptions\ValidationException;
use PHPUnit\Framework\TestCase;

class ClientTest extends TestCase
{
    private Client $client;

    protected function setUp(): void
    {
        $this->client = new Client([
            'api_key' => 'test_key',
            'base_url' => 'https://api.kirimel.com/v2'
        ]);
    }

    public function testClientInstantiation(): void
    {
        $this->assertInstanceOf(Client::class, $this->client);
    }

    public function testCampaignsResourceExists(): void
    {
        $this->assertInstanceOf(\KiriMel\Resources\Campaigns::class, $this->client->campaigns());
    }

    public function testSubscribersResourceExists(): void
    {
        $this->assertInstanceOf(\KiriMel\Resources\Subscribers::class, $this->client->subscribers());
    }

    public function testMagicPropertyGetter(): void
    {
        $this->assertInstanceOf(\KiriMel\Resources\Campaigns::class, $this->client->campaigns);
        $this->assertInstanceOf(\KiriMel\Resources\Lists::class, $this->client->lists);
    }

    public function testUnknownResourceThrowsException(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->client->unknown_resource;
    }
}
