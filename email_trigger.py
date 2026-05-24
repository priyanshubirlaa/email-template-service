def trigger_affiliate_welcome(user):
    sfmc.send(
        template="AFFILIATEWELCOME",
        email=user.email
    )
retry_count =3
