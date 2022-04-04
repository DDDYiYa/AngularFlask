import { Component,OnInit } from '@angular/core';
import { CommonService } from './services/common.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend_Angular';

  constructor(private cs : CommonService ){}

  hello_string : string = '';
  
  ngOnInit()
  {
    this.cs.readhello().subscribe( r => this.hello_string = r)
  }

}
